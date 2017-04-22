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

template<typename T>
size_t decreseMax(T& arr, int except) {
   if (except >= 0 && arr[except] == (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5])) {

      if (arr[except] == 0) {
         printf("FFF");
      }
      --arr[except];
      return except;
   }
   size_t maxI = except==0? 1 : 0;
   for (size_t i = 0; i < 6; ++i) {
      if (i!= except && arr[i] > arr[maxI]) maxI = i;
   }
   if (arr[maxI] == 0) maxI = except;
   if (arr[maxI] == 0) {
      printf("FFF");
   }
   --arr[maxI];
   return maxI;
}

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int r, o, y, g, b, v;
   int n;
   cin >> n;
   cin >> r;
   cin >> o;
   cin >> y;
   cin >> g;
   cin >> b;
   cin >> v;

   int unic[6] = { r,o,y,g,b,v };
   vector<int> stable(n);

   
   if (o + g + v == 0) {
      stable[0] = decreseMax(unic, -1);
      for (size_t i = 1; i < n; ++i) {
         stable[i] = decreseMax(unic, stable[i-1]);
         if (stable[i] == stable[i - 1]) {
            printf("IMPOSSIBLE\n");
            return;
         }
      }
      if (stable[0] == stable[n - 1]) {
         printf("IMPOSSIBLE\n");
         return;
      }

      for (const auto& a : stable) {
         if (a == 0)
            printf("R");
         else if (a == 2)
            printf("Y");
         else  if (a == 4)
            printf("B");
         else printf("F");
         
      }

      printf("\n");


   }
   else
   { // big one
      printf("FUCK\n");
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
