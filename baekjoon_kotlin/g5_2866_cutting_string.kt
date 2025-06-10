/*
<2866. 문자열 잘라내기>
골드5
https://www.acmicpc.net/problem/2866
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(" ").map{ it.toInt() }
    val rowTable = Array(n) { readLine().toCharArray() }

    val colTable = mutableListOf<String>()
    for (i in 0 until k) {
        var temp: String = ""
        for (j in 0 until n) temp += rowTable[j][i]
        colTable.add(temp)
    }
    
    fun checkRepeat(cnt: Int): Boolean {
        val tempSet = mutableSetOf<String>()
        colTable.forEach{ item ->
            tempSet.add(item.drop(cnt))
        }
        return tempSet.size != k
    }
    
    var start = 0
    var end = n
    var result = 0
    while(start <= end) {
        val mid = (start + end) / 2
        if (checkRepeat(mid)) {
            end = mid - 1
        } else {
            result = mid
            start = mid + 1
        }
    }

    println(result)
}
