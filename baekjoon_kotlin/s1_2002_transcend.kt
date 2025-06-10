/*
<2002. 추월>
실버1
https://www.acmicpc.net/problem/2002
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val inCar = Array(n) {readLine()}
    val outCar = Array(n) {readLine()}

    val inOrder = mutableMapOf<String, Int>()
    inCar.forEachIndexed{ idx, item ->
        inOrder.put(item, idx)
    }

    val outOrder = mutableListOf<Int>()
    outCar.forEach{ item ->
        val inRank = inOrder[item] ?: 0
        outOrder.add(inRank)
    }

    var result = 0
    for (i in 0 until n) {
        for (j in i until n) {
            if (outOrder[i] > outOrder[j]) {
                result += 1
                break
            }
        }
    }
    println(result)
}