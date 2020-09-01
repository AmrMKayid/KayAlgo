package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT

	scanner := bufio.NewReader(os.Stdin)

	var T int
	fmt.Scan(&T)

	for ; T > 0; T-- {
		s, _ := scanner.ReadString('\n')
		n := len(s)

		var s_odd = ""
		var s_even = ""

		for i := 0; i < n; i++ {
			if i%2 == 0 {
				s_even += string(s[i])
			} else {
				s_odd += string(s[i])
			}
		}

		fmt.Printf("%v %v\n", strings.TrimSpace(s_even), strings.TrimSpace(s_odd))

	}
}
