/*
<2302. 극장 좌석>
실버1
https://www.acmicpc.net/problem/2302
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val m = readLine().toInt()
    val vips = IntArray(m) { readLine().toInt() }

    // 바꾸는 방법 DP
    val moves = IntArray(41)
    moves[0] = 1
    moves[1] = 1
    moves[2] = 2
    for (i in 3..40) {
        moves[i] = moves[i-1] + moves[i-2]
    }

    // 실제 가짓수 DP
    val dp = IntArray(n+1)
    dp[0] = 1
    var movable = 0

    for (i in 1..n) {
        if (i in vips) {
            movable = 0
            dp[i] = dp[i-1]
        } else {
            movable += 1
            dp[i] = dp[i-movable] * moves[movable]
        }
    }
    println(dp[n])
}