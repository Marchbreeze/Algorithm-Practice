/*
<1780. 종이의 개수>
실버2
https://www.acmicpc.net/problem/1780
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val paper = Array(n) { readLine().split(" ").map{ it.toInt() } }

    // 각 -1, 0, 1 갯수 저장
    val counts = IntArray(3) { 0 }

    fun divided(row: Int, col:Int, n:Int) {
        // 시작 지점의 값으로 부분집합 확인
        val item = paper[row][col]

        for (i in row until row+n) {
            for (j in col until col+n) {
                if (paper[i][j] != item) {
                    // 종이 9등분
                    val next = n / 3
                    divided(row, col, next)
                    divided(row, col+next, next)
                    divided(row, col+next+next, next)
                    divided(row+next, col, next)
                    divided(row+next, col+next, next)
                    divided(row+next, col+next+next, next)
                    divided(row+next+next, col, next)
                    divided(row+next+next, col+next, next)
                    divided(row+next+next, col+next+next, next)
                    return
                }
            }
        }
        counts[item+1] += 1
        return
    }

    divided(0, 0, n)
    counts.forEach { count ->
        println(count)
    }
}