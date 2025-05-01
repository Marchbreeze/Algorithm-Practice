/*
<14728. 벼락치기>
골드5
https://www.acmicpc.net/problem/14728
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, t) = readLine().split(" ").map{ it.toInt() }
    val tests = Array(n) {readLine().split(" ").map{ it.toInt() }.let{ (w, v) -> w to v }}
    
    val dp = IntArray(t+1) {0}
    tests.forEach { test ->
        val (time, value) = test
        for (i in t downTo time) {
            dp[i] = maxOf(dp[i], dp[i-time] + value)
        }
    }
    println(dp[t])
}