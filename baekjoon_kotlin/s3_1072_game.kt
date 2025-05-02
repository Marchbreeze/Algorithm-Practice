/*
<1072. 게임>
실버3
https://www.acmicpc.net/problem/1072
*/

import java.io.*
import java.util.*
import kotlin.math.*
import kotlin.system.exitProcess

private fun getFloor(up: Int, down: Int): Int {
    return floor(up * 100.0 / down).toInt()
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (x, y) = readLine().split(" ").map{ it.toInt() }
    val z = getFloor(y, x)
    if (z >= 99) {
        println(-1)
        exitProcess(0)
    }
    var start = 0
    var end = x
    var answer = 0
    while (start <= end) {
        val mid = (start + end) / 2
        if (getFloor(y+mid, x+mid) > z) {
            answer = mid
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    println(answer)
}