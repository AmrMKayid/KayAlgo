package main

/**
	factored import statement
 */
import (
	"fmt"
	"math"
	"math/rand"
	"math/cmplx"
	"runtime"
	"time"
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


	/*
	Go has only one looping construct, the for loop.
		there are no parentheses surrounding the three components of the for statement
		and the braces { } are always required.
	 */
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}

	fmt.Println(sum)



	/*
		like While loop & drop the semicolons;
	 */
	sum2 := 1
	for ; sum2 < 1000; {
		sum2 += sum2
	}
	fmt.Println(sum2)


	/*
		Go's switch cases need not be constants, and the values involved need not be integers.
	 */
	fmt.Print("Kayid runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("macOS")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.", os)
	}

	/*
		Switch with no condition
	 */
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}


	/*
		A defer statement defers the execution of a function until the surrounding function returns.
	 */
	defer fmt.Println("world")

	fmt.Println("hello")


	/*
		Last-in-First-out execution!
	 */
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
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
