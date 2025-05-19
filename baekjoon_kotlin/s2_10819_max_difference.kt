/*
<10819. 차이를 최대로>
실버2
https://www.acmicpc.net/problem/10819
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val nums = readLine().split(" ").map{ it.toInt() }

    val temp = mutableListOf<Int>()
    val visited = BooleanArray(n+1)
    var result = 0

    fun dfs() {
        if (temp.size == n) {
            var count = 0
            for (i in 1 until n) {
                count += abs(temp[i] - temp[i-1])
            }
            if (count > result) result = count
            return
        }
        nums.forEachIndexed { idx, num ->
            if (!visited[idx]){
                visited[idx] = true
                temp.add(num)
                dfs()
                temp.removeLast()
                visited[idx] = false
            }
        }
    }

    dfs()
    println(result)
}