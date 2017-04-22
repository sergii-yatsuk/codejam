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
#include <unordered_set>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   printf("Case #%d: \n", test + 1);
   int rows, cols;
   cin >> rows;
   cin >> cols;
   vector<string> cake(rows);

   string row;
   unordered_set<char> used;
   for (size_t i = 0; i < rows; ++i) {
      cin >> row;
      cake[i] = row;
   }

   char c;
   for (size_t row = 0; row < rows; ++row) {
      for (size_t col = 0; col < cols; ++col) {
         c = cake[row][col];
         if (c!='?' && used.count(c) == 0) {
            used.insert(c);
            bool used = false;

            int colNew = col + 1;
            while (colNew < cols && cake[row][colNew] == '?') {
               cake[row][colNew] = c;
               ++colNew;
               used = true;
            }

            colNew = col - 1;
            while (colNew >= 0 && cake[row][colNew] == '?') {
               cake[row][colNew] = c;
               --colNew;
               used = true;
            }

            int rownew = row + 1;
            while (!used && rownew < rows && cake[rownew][col] == '?') {
               cake[rownew][col] = c;
               ++rownew;
            }
            rownew = row - 1;
            while (!used && rownew >= 0 && cake[rownew][col] == '?') {
               cake[rownew][col] = c;
               --rownew;
            }


         }
      }
   }


   for (size_t row = 0; row < rows; ++row) {
      if (cake[row].find('?') != string::npos) {
         int col = cake[row].find('?');
         int newRow;
         if (row > 0) {
            newRow = row - 1;
         }
         else {
            newRow = row + 1;
         }
         if (col ==0 || cake[newRow][col - 1] == cake[row][col - 1]) {
            for (int newCol = col; newCol < cols && cake[row][newCol] == '?' ; ++newCol) {
               cake[row][newCol] = cake[newRow][newCol];
            }
         }

      }
   }



   for (size_t i = 0; i < rows; ++i) {
      cout << cake[i] << "\n";
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
