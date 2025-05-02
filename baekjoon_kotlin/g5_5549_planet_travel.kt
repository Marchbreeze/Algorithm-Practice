/*
<5549. 행성 탐사>
골드5
https://www.acmicpc.net/problem/5549
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (m, n) = readLine().split(" ").map{ it.toInt() }
    val k = readLine().toInt()
    val arr = Array(m) { readLine().toCharArray() }
    
    // 누적합 세팅
    val hapJ = Array(m+1) { IntArray(n+1) }
    val hapO = Array(m+1) { IntArray(n+1) }
    val hapI = Array(m+1) { IntArray(n+1) }
    for (y in 1..m) {
        for (x in 1..n) {
            hapJ[y][x] = hapJ[y-1][x] + hapJ[y][x-1] - hapJ[y-1][x-1]
            hapO[y][x] = hapO[y-1][x] + hapO[y][x-1] - hapO[y-1][x-1]
            hapI[y][x] = hapI[y-1][x] + hapI[y][x-1] - hapI[y-1][x-1]
            when (arr[y-1][x-1]) {
                'J' -> hapJ[y][x] += 1
                'O' -> hapO[y][x] += 1
                'I' -> hapI[y][x] += 1
            }
        }
    }

    // 결과 출력
    repeat(k) {
        val (a, b, c, d) = readLine().split(" ").map{ it.toInt() }
        val answerJ = hapJ[c][d] - hapJ[a - 1][d] - hapJ[c][b - 1] + hapJ[a - 1][b - 1]
        val answerO = hapO[c][d] - hapO[a - 1][d] - hapO[c][b - 1] + hapO[a - 1][b - 1]
        val answerI = hapI[c][d] - hapI[a - 1][d] - hapI[c][b - 1] + hapI[a - 1][b - 1]
        println("$answerJ $answerO $answerI")
    }
}