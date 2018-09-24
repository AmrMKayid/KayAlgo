package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			countLines(f, counts)
			// Exercise 1.4: Modify dup2 to print the names of all files
			// in which each duplicated line occurs.
			for _, n := range counts {
				if n > 1 {
					counts[arg] = -1
					break
				}
			}
			f.Close()
		}
	}

	fmt.Println("Files")
	for line, n := range counts {
		if n == -1 {
			fmt.Printf("%s\n", line)
		}
	}
	fmt.Println("\n#--------------------#\n")
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("count: %d \t Line: %s\n", n, line)
		}
	}
}

func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}
	// NOTE: ignoring potential errors from input.Err()
}