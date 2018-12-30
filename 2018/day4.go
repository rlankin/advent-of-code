package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"time"
)

type event struct {
	t     time.Time
	event string
}

func main() {
	guards := getGuardData()

	// TODO: Parallelize with goroutines+channels?
	var maxSleepTime, maxSleepGuardID, mostCommonMin int
	for guardID, sleepMins := range guards {
		if len(sleepMins) > maxSleepTime {
			maxSleepTime, maxSleepGuardID = len(sleepMins), guardID
			mostCommonMin, _ = getMostCommonMinute(sleepMins)
		}
	}

	fmt.Printf("Part 1: %d\n", maxSleepGuardID*mostCommonMin)

	maxSleepTime = 0
	mostCommonMin = 0
	for guardID, sleepMins := range guards {
		min, c := getMostCommonMinute(sleepMins)
		if c > maxSleepTime {
			maxSleepTime = c
			mostCommonMin = min
			maxSleepGuardID = guardID
		}
	}

	fmt.Printf("Part 2: %d\n", maxSleepGuardID*mostCommonMin)
}

func getMostCommonMinute(minutes []time.Time) (int, int) {
	var mostCommonMin int

	// Tally up minute counts
	minHist := make(map[int]int)
	for _, m := range minutes {
		minHist[m.Minute()]++
	}
	// Find most common minute
	var count int
	for m, c := range minHist {
		if c > count {
			count = c
			mostCommonMin = m
		}
	}

	return mostCommonMin, count
}

func getGuardData() map[int][]time.Time {
	const TimeFormat = "2006-01-02 15:04"
	oneMinute, _ := time.ParseDuration("1m")

	c := make(chan string)
	go readLines("input/day4_input", c)

	// Read schedule in
	regex := regexp.MustCompile("\\[(.*)\\] (.*)")
	var schedule []event
	for line := range c {
		matches := regex.FindStringSubmatch(line)
		time, _ := time.Parse(TimeFormat, matches[1])
		schedule = append(schedule, event{time, matches[2]})
	}
	sort.Slice(schedule, func(i, j int) bool {
		return schedule[i].t.Before(schedule[j].t)
	})

	// Parse schedule
	guards := make(map[int][]time.Time)
	regex = regexp.MustCompile("([\\S]+) #?([\\S]+)(?: .*)?")
	var guardID int
	var sleepTime time.Time
	for _, e := range schedule {
		matches := regex.FindStringSubmatch(e.event)
		if matches[1] == "Guard" {
			guardID, _ = strconv.Atoi(matches[2])
		} else if matches[1] == "falls" {
			sleepTime = e.t
		} else if matches[1] == "wakes" {
			for sleepTime.Before(e.t) {
				guards[guardID] = append(guards[guardID], sleepTime)
				sleepTime = sleepTime.Add(oneMinute)
			}
		}
	}

	return guards
}

func readLines(fileName string, c chan string) {
	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		c <- scanner.Text()
	}

	close(c)
}
