package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
)

func main() {
  	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".
  
    var i uint64 = 4
    var d float64 = 4.0
    var s string = "HackerRank "

    scanner := bufio.NewScanner(os.Stdin)


    // Declare second integer, double, and String variables.
    var (
        i2 uint64
        d2 float64
        s2 string
    )
    // Read and save an integer, double, and String to your variables.
    for i := 1; i <= 3 && scanner.Scan(); i++ {
        switch i {
        case 1:
            i2, _ = strconv.ParseUint(scanner.Text(), 10, 64)
        case 2:
            d2, _ = strconv.ParseFloat(scanner.Text(), 64)
        case 3:
            s2 = scanner.Text()
        }
    }

    // Print the sum of both integer variables on a new line.
    fmt.Println(i + i2)
    // Print the sum of the double variables on a new line.
    fmt.Printf("%0.1f\n", d + d2)
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    fmt.Println(s + s2)
}