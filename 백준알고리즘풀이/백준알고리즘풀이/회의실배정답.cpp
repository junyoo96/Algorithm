#include <cstdio>
#include <algorithm>
using namespace std;

typedef pair<int, int> meeting;

char buf[1 << 14];
int idx, nidx;

char read()
{
	if (idx == nidx) {
		nidx = fread(buf, 1, 1 << 14, stdin);
		idx = 0;
	}
	return buf[idx++];
}
int readInt()
{
	int sum = 0;
	char now = read();
	while (now == ' ' || now == '\n') now = read();
	while (now >= '0' && now <= '9') {
		sum = sum * 10 + now - 48;
		now = read();
	}

	return sum;
}
int main()
{
	int n = readInt();

	meeting m[100000];
	for (int tc = 0; tc < n; ++tc) {
		m[tc].second = readInt();
		m[tc].first = readInt();
	}

	std::sort(m, m + n);

	int ans = 1;
	int prev = 0;
	for (int i = 1; i < n; ++i) {
		if (m[i].second >= m[prev].first) {
			prev = i;
			ans++;
		}
	}

	printf("%d", ans);

	return 0;
}