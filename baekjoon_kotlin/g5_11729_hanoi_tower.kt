/*
<11729. 하노이 탑 이동 순서>
골드5
https://www.acmicpc.net/problem/11729
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val n = br.readLine().toInt()
    // 총 이동 횟수 계산 및 출력
    bw.write("${(2.0.pow(n) - 1).toLong()}\n")

    // 재귀로 Hanoi 이동 경로를 버퍼에 기록
    fun moveStacks(from: Int, to: Int, height: Int) {
        if (height == 1) {
            bw.write("$from $to\n")
        } else {
            val aux = 6 - from - to
            moveStacks(from, aux, height - 1)
            bw.write("$from $to\n")
            moveStacks(aux, to, height - 1)
        }
    }

    moveStacks(1, 3, n)
    bw.flush()
}