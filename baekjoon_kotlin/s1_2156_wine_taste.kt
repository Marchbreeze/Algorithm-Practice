/*
<2156. 포도주 시식>
실버1
https://www.acmicpc.net/problem/2156
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val wine = mutableListOf<Int>(0)
    repeat(n) { wine.add(readLine().toInt()) }

    // d[2] : oo
    // d[3] : oox, oxo, xoo
    // d[4] : o.oxo, o.xoo, x.oox
    // d[5] : oo.xoo, oxoo.x, xoo.xo
    val d = IntArray(n+1) { 0 }
    d[1] = wine[1]
    if (n > 1) d[2] = wine[1] + wine[2]
    for (i in 3..n){
        d[i] = maxOf(d[i-1], d[i-2]+wine[i], d[i-3]+wine[i-1]+wine[i])
    }
    println(d[n])
}