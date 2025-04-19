/*
<13913. 숨바꼭질4>
골드4
https://www.acmicpc.net/problem/13913
*/

import java.io.*
import java.util.*

// 1차원 직선(0~100,000)에서 N에서 K까지 가는 최소시간 / +1, -1, *2 가능
// 직전 위치 정보를 저장하면서 모든 경로 저장
// 배열에 카운트와 직전 위치 정보 담아서 BFS 진행

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    // 입력
    val (n, k) = readLine().split(" ").map { it.toInt() }
    // 횟수 기록 (100,000회, 직전 위치 -1로 모두 초기화)
    val d = Array(100001) { 100000 to -1 }
    d[n] = 0 to -1

    // 큐 생성
    val q = LinkedList<Int>()
    q.offer(n)

    // BFS 진행
    while (q.isNotEmpty()) {
        val count = q.poll()
        if (count < 100000 && d[count + 1].first > d[count].first) {
           d[count + 1] = d[count].first + 1 to count
           q.offer(count + 1)
        }
        if (count > 0 && d[count - 1].first > d[count].first) {
            d[count - 1] = d[count].first + 1 to count
            q.offer(count - 1)
        }
        if (count < 50001 && d[count * 2].first > d[count].first) {
            d[count * 2] = d[count].first + 1 to count
            q.offer(count * 2)
        }
    }

    // 결과 출력
    println(d[k].first)

    // 경로 뒤로 쫒기
    val route = mutableListOf(k)
    for (i in (0..d[k].first - 1)) {
        route.add(d[route.last()].second)
    }
    route.reverse()
    println(route.joinToString(separator = " ") { it.toString() })
}