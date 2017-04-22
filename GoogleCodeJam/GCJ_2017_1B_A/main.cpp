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
   int d, k;
   cin >> d;
   cin >> k;
   
   int h1p;
   int h1s;

   int h2p;
   int h2s;

   cin >> h1p;
   cin >> h1s;

   if (k > 1) {
      cin >> h2p;
      cin >> h2s;
   }

   if (k == 1) {
      double h1t = double(d - h1p) / double(h1s);
      double result = double(d) / h1t;
      printf("%.6f\n", result);
      return;
   }
   else {
      if (h2p < h1p) {
         swap(h1p, h2p);
         swap(h1s, h2s);
      }

      double h1t = double(d - h1p) / double(h1s);
      double h2t = double(d - h2p) / double(h2s);

      if (h1t >= h2t) {
         double result = double(d) / h1t;
         printf("%.6f\n", result);
         return;
      }else {
         double t = double(h2p - h1p) / double(h1s - h2s);
         double p = double(h1p) + double(h1s)*t;
         double t2 = double(d-p) / double(min(h1s, h2s));
         double result = double(d) / (t+t2);
         printf("%.6f\n", result);
         return;
      }
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
