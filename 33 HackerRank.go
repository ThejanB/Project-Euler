// Go version of the python code
// 100%

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func insert(array []byte, count int, target byte) []byte {
	newArr := make([]byte, count+len(array))
	for k := 0; k < count; k++ {
		newArr[k] = target
	}
	copy(newArr[count:], array)
	return newArr
}

func nextPermutation(a []byte) bool {
	i := len(a) - 1
	for i > 0 && a[i-1] >= a[i] {
		i--
	}
	if i <= 0 {
		return false
	}

	j := len(a) - 1
	for a[j] <= a[i-1] {
		j--
	}

	a[i-1], a[j] = a[j], a[i-1]

	for j, k := i, len(a)-1; j < k; j, k = j+1, k-1 {
		a[j], a[k] = a[k], a[j]
	}
	return true
}

func numToCharArray(x, digits int) []byte {
	s := fmt.Sprintf("%0*d", digits, x)
	return []byte(s)
}

func merge(strFill, mask []byte) int {
	index := 0
	result := 0
	for _, m := range mask {
		result *= 10
		if m == '.' {
			result += int(strFill[index] - '0')
			index++
		} else {
			result += int(m - '0')
		}
	}
	return result
}

func clone(s []byte) []byte {
	cp := make([]byte, len(s))
	copy(cp, s)
	return cp
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	scanner.Scan()
	inputLine := scanner.Text()
	parts := strings.Fields(inputLine)
	if len(parts) < 2 {
		fmt.Println("Please provide two integers N and K.")
		return
	}
	N, err1 := strconv.Atoi(parts[0])
	K, err2 := strconv.Atoi(parts[1])
	if err1 != nil || err2 != nil {
		fmt.Println("Invalid input.")
		return
	}
	keep := N - K

	// Tens array for base powers up to 10^4.
	Tens := []int{1, 10, 100, 1000, 10000}
	sumN := 0
	sumD := 0
	used := make(map[int]bool)

	for d := 1; d < Tens[keep]; d++ {
		for n := 1; n < d; n++ {
			charN := numToCharArray(n, keep)
			charD := numToCharArray(d, keep)
			for i := Tens[K-1]; i < Tens[K]; i++ {
				in := numToCharArray(i, K)
				isAscending := true
				for j := 1; j < len(in); j++ {
					if in[j-1] > in[j] {
						isAscending = false
						break
					}
				}
				if !isAscending {
					continue
				}
				pattern := insert(in, keep, '.')
				charInsertN := clone(pattern)
				for {
					newN := merge(charN, charInsertN)
					if newN >= Tens[N-1] {
						charInsertD := clone(pattern)
						for {
							newD := merge(charD, charInsertD)
							if newN*d == newD*n {
								id := newN*10000 + newD
								if !used[id] {
									sumN += newN
									sumD += newD
									used[id] = true
								}
							}
							if !nextPermutation(charInsertD) {
								break
							}
						}
					}
					if !nextPermutation(charInsertN) {
						break
					}
				}
			}
		}
	}
	fmt.Println(sumN, sumD)
}
