/*
<15650. N과 M (2)>
실버3
https://www.acmicpc.net/problem/15650
*/

import java.io.*
import java.util.*

private val temp = mutableListOf<Int>()

private fun dfs(given: Int, n: Int, m:Int) {
    if (temp.size == m) {
        println(temp.joinToString(" "))
        return
    }
    for (num in given..n) {
        temp.add(num)
        dfs(num+1, n, m)
        temp.removeLast()
    }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(" ").map { it.toInt() }
    dfs (1, n, m)
}