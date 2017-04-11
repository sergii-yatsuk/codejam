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

bool isTidy(ll n) {
   int prev = n % 10;
   n = n / 10;
   while (n) {
      if (n % 10 > prev) return false;
      prev = n % 10;
      n = n / 10;
   }
   return true;
}

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   long long n;
   cin >> n;

   while (n) {
      if (isTidy(n)) {
         printf("%llu\n", n);
         break;
      }
      --n;
   }

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
