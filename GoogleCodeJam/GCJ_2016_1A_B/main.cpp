// https://code.google.com/codejam/contest/4304486/dashboard#s=p1

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

bool tryAsRow(vector<vector<int>>& grid, vector<int>& row, size_t i, bool put=false) {
   for (size_t j = 0; j < row.size(); ++j) {
      if (grid[i][j] && grid[i][j] != row[j]) return false;
      if (i > 0 && !grid[i][j] && grid[i - 1][j] >= row[j]) return false;
      if (put && !grid[i][j]) grid[i][j] = row[j];
   }
   return true;

}

bool tryAsCol(vector<vector<int>>& grid, vector<int>& col, size_t j, bool put = false) {
   for (size_t i = 0; i < col.size(); ++i) {
      if (grid[i][j] && grid[i][j] != col[i]) return false;
      if (j > 0 && !grid[i][j] && grid[i][j - 1] >= col[i]) return false;
      if (put && !grid[i][j]) grid[i][j] = col[i];
   }
   return true;

}

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int N;
   cin >> N;

   vector<vector<int>> papers(2 * N - 1);

   for (int i = 0; i < 2 * N - 1; ++i) {
      vector<int> arr(N);
      for (int j = 0; j < N; ++j) {
         cin >> arr[j];
      }
      papers[i] = arr;
   }

   sort(papers.begin(), papers.end());

   vector<vector<int>> grid(N, vector<int>(N, 0));

   vector<bool> usedRows(N, false);
   vector<bool> usedCols(N, false);
   size_t curR = 0;
   size_t curC = 0;
   bool b = true;

   for (int i = 0; i < papers.size(); ++i) {
      if (b) {
         for (int r = 0; r < N; ++r) {
            if (tryAsRow(grid, papers[i], r)) {
               usedRows[r] = true;
               tryAsRow(grid, papers[i], r, true);
               ++curR;
            }
            else if (tryAsCol(grid, papers[i], r)) {
               usedCols[r] = true;
               tryAsCol(grid, papers[i], r, true);
               ++curC;
            }
         }

         b = !b;
      }
      else {
         for (int r = 0; r < N; ++r) {
            if (tryAsCol(grid, papers[i], r)) {
               usedCols[r] = true;
               tryAsCol(grid, papers[i], r, true);
               ++curC;
            }
            else if (tryAsRow(grid, papers[i], r)) {
               usedRows[r] = true;
               tryAsRow(grid, papers[i], r, true);
               ++curR;
            }
         }

         b = !b;

      }
   }

   for (int i = 0; i < N; ++i) {
      if (!usedRows[i]) {
         for (int j = 0; j < N; ++j) {
            cout << grid[i][j] << " ";
         }
         cout << "\n";
         break;
      }
      else if (!usedCols[i]) {
         for (int j = 0; j < N; ++j) {
            cout << grid[j][i] << " ";
         }
         cout << "\n";
         break;
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
