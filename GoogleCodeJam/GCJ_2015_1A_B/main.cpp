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

ll gcd(ll a, ll b)
{
   if (b == 0)
      return a;
   return gcd(b, a%b);
}

ll findLCM(vector<int>& vec) {
   ll ans = vec[0];

   for (ll i = 1; i < vec.size(); i++)
      ans = (((vec[i] * ans)) /
      (gcd(vec[i], ans)));

   return ans;
}

void solve(ll test)
{
   printf("Case #%d: ", test + 1);
   ll B, N;
   cin >> B;
   cin >> N;

   int minT = 100000;
   int newMinT = 100000;
   vector<int> m(B);
   for (int i = 0; i < B; ++i) {
      cin >> m[i];
      minT = min(minT, m[i]);
   }

   ll processed = 0;
   ll lcm = findLCM(m);
   for (int i = 0; i < B; ++i) {
      processed += lcm / m[i];
   }


   N = N % processed;
   if (N == 0) {
      printf("%d\n", B);
      return;
   }

   vector<int> q(B);

   int lastI = -1;
   while (N > 0) {
      // place people
      for (ll i = 0; i < B && N>0; ++i) {
         if (q[i] == 0) {
            q[i] = m[i];
            --N;
            lastI = i;
         }
      }

      // make haircut
      newMinT = 100000;
      for (int  i = 0; i < B; ++i) {
         q[i] = q[i] - minT;
         newMinT = min(newMinT, q[i]);
      }
      minT = newMinT;
   }
   printf("%d\n", lastI+1);
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
