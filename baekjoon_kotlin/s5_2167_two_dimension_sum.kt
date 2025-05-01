/*
<2167. 2차원 배열의 합>
실버5
https://www.acmicpc.net/problem/1451
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    val arr = Array(n) { readLine().split(" ").map{ it.toInt() } }
    
    // 누적합 (크기 + 1인 테이블)
    val hap = Array(n+1) { IntArray(m+1) { 0 } }
    for (y in 1..n) {
        for (x in 1..m) {
            hap[y][x] = arr[y-1][x-1] + hap[y][x-1] + hap[y-1][x]- hap[y-1][x-1]
        }
    }

    val t = readLine().toInt()
    repeat(t) {
        val (i, j, x, y) = readLine().split(" ").map{ it.toInt() }
        println(hap[x][y] - hap[i-1][y] - hap[x][j-1] + hap[i-1][j-1])
    }
}