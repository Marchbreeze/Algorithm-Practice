/*
<2688. 줄어들지 않아>
실버1
https://www.acmicpc.net/problem/2688
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){

    // 1 : [1,1,1,1,1,1,1,1,1,1,1]
    // 2 : [1,2,3,4,5,6,7,8,9,10]
    // 3 : [1,3,6,10,...]
    val dp = LongArray(65)
    dp[1] = 10L
    val dpDigit = LongArray(11) { 1L }

    for (i in 2..64) {
        var total = 0L
        for (j in 0..9) {
            var sum = 0L
            for (k in j..9) {
                sum += dpDigit[k]
            }
            dpDigit[j] = sum
            total += sum
        }
        dp[i] = total
    }

    val t = readLine().toInt()
    repeat(t) {
        val n = readLine().toInt()
        println(dp[n])
    }
}