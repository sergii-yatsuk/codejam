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
   ll n;
   ll k;
   cin >> n;
   cin >> k;
   //cout << n << " " << k << " ";
   if (k == 1) {
      printf("%lld %lld\n", n - (n-1)/2-1, (n - 1) / 2);
      return;
   }
   if (k == n) {
      printf("0 0\n");
      return;
   }

   ll usedLevels = int(log(k+1) / log(2));
   ll defenetlyUsed = pow(2, usedLevels) - 1;


   ll distanceFirst = n / pow(2, usedLevels-1);
   ll distanceLast = distanceFirst - 1;

   if (k == defenetlyUsed) {
      if ((ll(n / pow(2, usedLevels - 1)) % 2 == 1)) {
         distanceFirst = (distanceFirst - 1) / 2;
         distanceLast = n / pow(2, usedLevels) - distanceFirst - 1;
      }
      else {
         distanceFirst = (distanceLast - 1) / 2;
         distanceLast = distanceLast - distanceFirst - 1;
      }
   }
   else {
      distanceFirst = n / pow(2, usedLevels);
      distanceLast = distanceFirst-1;
      ll rest = k - defenetlyUsed;

      //if (rest == pow(2, usedLevels+1))

      if ((ll(n / pow(2, usedLevels - 1)) % 2 == 1)) {
         distanceFirst = (distanceFirst - 1) / 2;
         distanceLast = n / pow(2, usedLevels) - distanceFirst - 1;
      }
      else {
         if (rest == 1) {
            distanceFirst = (distanceFirst - 1) / 2;
            distanceLast = n / pow(2, usedLevels) - distanceFirst - 1;
         }
         else {
            distanceFirst = (distanceLast - 1) / 2;
            distanceLast = n / pow(2, usedLevels) - distanceFirst - 2;
         }
      }

   }

   printf("%lld %lld\n", max(distanceFirst, distanceLast), min(distanceFirst, distanceLast));
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
