/*
<19949. 영재의 시험>
실버1
https://www.acmicpc.net/problem/19949
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val answer = readLine().split(" ").map{ it.toInt() }
    val temp = mutableListOf<Int>()
    var score = 0
    var count = 0

    fun checkRepeat(num: Int): Boolean {
        if (temp.size < 2) return false
        val lastTwo = temp.takeLast(2)
        return lastTwo[0] == lastTwo[1] && lastTwo[1] == num
    }

    fun dfs() {
        if (temp.size == 10) {
            if (score >= 5) count += 1
            return
        }
        for (num in 1..5) {
            if (!checkRepeat(num)) {
                temp.add(num)
                val isAnswer = if(num == answer[temp.size - 1]) 1 else 0
                score += isAnswer
                dfs()
                score -= isAnswer
                temp.removeLast()
            }
        }
    }

    dfs()
    println(count)
}