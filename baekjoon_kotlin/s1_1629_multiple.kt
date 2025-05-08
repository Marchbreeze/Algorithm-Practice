/*
<1629. 곱셈>
실버1
https://www.acmicpc.net/problem/1629
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var (a, b, c) = readLine().split(' ').map { it.toLong() }
    var result = 1L
    while (b > 0) {
        if (b % 2 == 1L) result = (result * a) % c
        a = (a * a) % c
        b /= 2
    }
    println(result)
}