/*
<11501. 주식>
실버2
https://www.acmicpc.net/problem/11501
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val t = readLine().toInt()
    repeat(t) {
        val n = readLine().toInt()
        val stocks = readLine().split(" ").map{ it.toInt() }.toMutableList()
        stocks.reverse()

        var result = 0L
        var currentMax = 0
        for (i in 0 until n) {
            if (stocks[i] > currentMax) {
                currentMax = stocks[i]
            } else {
                result += currentMax - stocks[i]
            }
        }
        println(result)
    }
}