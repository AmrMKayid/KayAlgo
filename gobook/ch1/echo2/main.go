package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// short variable declaration
	s, sep := "", ""

	// iterates over a range of values
	for index, arg := range os.Args[1:] {
		s += sep + "[" + strconv.Itoa(index) + "] -> " + arg
		sep = "\n"
	}
	fmt.Println(s)
}
