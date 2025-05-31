/*
<14430. 자원 캐기>
실버2
https://www.acmicpc.net/problem/14430
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    val area = Array(n) {readLine().split(" ").map{ it.toInt() } }
    
    val dp = Array(n+1) { IntArray(m+1) }
    for (y in 1..n) {
        for (x in 1..m) {
            dp[y][x] = area[y-1][x-1] + maxOf(dp[y-1][x], dp[y][x-1]) 
        }
    }
    println(dp[n][m])
}