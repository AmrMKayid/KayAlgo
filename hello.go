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


type Vertex struct {
	X int
	Y int
}


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


	fmt.Println(Vertex{3, 7})

	/*
		Pointers to structs
	 */
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)


	var (
		v1 = Vertex{1, 2}  // has type Vertex
		v2 = Vertex{X: 1}  // Y:0 is implicit
		v3 = Vertex{}      // X:0 and Y:0
		pV  = &Vertex{1, 2} // has type *Vertex
	)

	fmt.Println(v1, pV, v2, v3)


	var arr [2]string
	arr[0] = "Hello, "
	arr[1] = "World!"

	fmt.Println(arr)


	// Slice literals
	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)



	/*
		dynamically-sized arrays.
	 */
	a2 := make([]int, 5)
	printSlice("a", a2)

	b2 := make([]int, 0, 5)
	printSlice("b", b2)


	var s2 []int
	printSlice("Before Appending", s2)

	// We can add more than one element at a time.
	s2 = append(s2, 2, 3, 4)
	printSlice("After Appending", s2)


	/*
		Range
	 */

	var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}


	/*
		A map maps keys to values.
	 */
	var m map[string]Vertex

	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40, -74,
	}
	fmt.Println(m)
	fmt.Println(m["Bell Labs"])



	fib := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(fib())
	}

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


func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}


// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	prev := 0
	next := 1
	return func() int {
		fib := next + prev
		prev = next
		next = fib
		return fib
	}
}