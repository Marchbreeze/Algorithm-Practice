/*
<1793. 타일링>
실버2
https://www.acmicpc.net/problem/1793
*/

/*
Int (32bit) : 최대 2,147,483,647 (2³¹ - 1)
Long (64bit) : 최대 9,223,372,036,854,775,807 (2⁶³ - 1)
BigInteger : 제한 없음 (import java.math.BigInteger)

문제 예제에서 Long의 최대 범위를 초과하는 출력이 존재 -> BigInteger 사용 필요
> 200
> 1071292029505993517027974728227441735014801995855195223534251
*/

import java.io.*
import java.util.*
import java.math.BigInteger

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val dp = Array(251) { BigInteger.ZERO }
    dp[0] = BigInteger.ONE
    dp[1] = BigInteger.ONE
    dp[2] = BigInteger.valueOf(3)

    for (i in 3..250) {
        dp[i] = dp[i - 1] + dp[i - 2] * BigInteger.valueOf(2)
    }

    while (true) {
        try {
            val n = readLine()
            if (n.isNullOrEmpty()) break
            println(dp[n.toInt()])
        } catch (e: Exception) {
            break
        }
    }
}