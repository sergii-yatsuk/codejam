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
   int N;
   cin >> N;
   vector<int> m(N);
   for (int i = 0; i < N; ++i) {
      cin >> m[i];
   }
   size_t mSz = m.size();

   int firstMethod = 0;

   for (int i = 1; i < mSz; ++i) {
      if (m[i] < m[i - 1]) firstMethod = firstMethod + m[i - 1] - m[i];
   }

   int minRate = m[0]-m[1];
   for (int i = 1; i < mSz; ++i) {
      if (m[i] < m[i - 1])  minRate = max(minRate, m[i - 1] - m[i]);
   }

   int secondMethod = 0;
   for (int i = 0; i < mSz-1; ++i) {
      secondMethod += min(m[i], minRate);
   }


   printf("%d %d\n", firstMethod, secondMethod);
}

int main()
{
   freopen("A-large-practice.in", "r", stdin);
   freopen("A-large-practice.out", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
