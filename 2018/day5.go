package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("input/day5_input")
	polymer := strings.TrimSpace(string(bytes))
	// polymer := "dabAcCaCBAcCcaDA" // TODO: Testing

	part1(polymer)
	part2(polymer)
}

func part1(polymer string) {
	result := react(polymer)
	fmt.Printf("Part 1: %d\n", len(result))
}

func part2(polymer string) {
	var channels []chan int
	for unit := 65; unit < 91; unit++ {
		c := make(chan int)
		channels = append(channels, c)
		go func(unit int, c chan int) {
			newPolymer := strings.Replace(polymer, string(unit), "", -1)
			newPolymer = strings.Replace(newPolymer, string(unit+32), "", -1)
			newPolymer = react(newPolymer)
			c <- len(newPolymer)
			close(c)
		}(unit, c)
	}

	min := -1
	for _, c := range channels {
		size := <-c
		if size < min || min == -1 {
			min = size
		}
	}

	fmt.Printf("Part 2: %d\n", min)
}

func react(polymer string) string {
	result := polymer
	for i := 0; i < len(result)-1; i++ {
		if result[i]+32 == result[i+1] || result[i]-32 == result[i+1] {
			result = result[:i] + result[i+2:]
			i -= 2
			if i < 0 {
				i = -1
			}
		}
	}
	return result
}
