/*
<15649. N과 M (1)>
실버3
https://www.acmicpc.net/problem/15649
*/

import java.io.*
import java.util.*

private val temp = mutableListOf<Int>()
private lateinit var visited: BooleanArray

private fun dfs(n: Int, m:Int) {
    if (temp.size == m) {
        println(temp.joinToString(" "))
        return
    }
    for (num in 1..n) {
        if (!visited[num]){
            visited[num] = true
            temp.add(num)
            dfs(n, m)
            temp.removeLast()
            visited[num] = false
        }
    }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(" ").map { it.toInt() }
    visited = BooleanArray(n+1)
    dfs (n, m)
}