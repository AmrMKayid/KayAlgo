package main

/**
	factored import statement
 */
import (
	"fmt"
	"math"
	"math/rand"
	"math/cmplx"
)

// package level
var c, python, java bool

// Basic types
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)


func main() {
	fmt.Println("Hello, World")
	fmt.Println("Welcome to Algorithms Design in GoLang")
	fmt.Println("Fav. Num: ", rand.Intn(7))
	fmt.Printf("Math Sqrt: %g\n", math.Sqrt(7))

	/**
		Exported names, a name is exported if it begins with a capital letter.
	 */
	//fmt.Println(math.pi)	Any "unexported" names are not accessible from outside the package.

	fmt.Println("Math Pi: ", math.Pi)

	/**
		Functions
	 */
 	fmt.Println(add(3, 4))

	fmt.Println(newAdd(3, 4))

 	a, b := swap("hello", "world")
 	fmt.Println(a, b)

	fmt.Println(split(17))

	var i int
	fmt.Println(i, c, python, java)

 	var j = 7
 	var k, l, test = false, true, "test"
 	fmt.Println(j, k, l, test)

 	amr := "Amr M. Kayid"
 	fmt.Println(amr)

	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)

	// Type conversions
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	fmt.Println(x, y, z)


	const Pi = 3.14
	fmt.Println("Happy", Pi, "Day")


}

func add(x int, y int) int {
	return x + y
}

func newAdd(x, y int) int {
	return x + y
}


// Multiple results
func swap(x, y string) (string, string) {
	return y, x
}

// "naked" return
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
