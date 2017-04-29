#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>
#include <array>
#include <cmath>
#include <limits>
#include <cassert>
#include <math.h>
#include <memory.h>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int n;
   cin >> n;

   priority_queue<pair<int,char>> q;
   int ci;
   int cnt=0;
   for (char c = 'A'; c < 'A' + n; ++c) {
      cin >> ci;
      q.push(make_pair(ci, c));
      cnt += ci;
   }

   if (cnt % 2 == 1) {
      pair<int, char> t = q.top();
      q.pop();

      cout << t.second << " ";
      --t.first;
      if (t.first > 0)
         q.push(t);
   }

   while (!q.empty()) {
      pair<int, char> t = q.top();
      q.pop();

      cout << t.second;
      --t.first;
      if (t.first>0)
         q.push(t);

      if (!q.empty()) {
         t = q.top();
         q.pop();
         cout << t.second;
         --t.first;
         if (t.first > 0)
            q.push(t);
      }

      cout << " ";

   }

   printf("\n");
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
