#include <cstdio>

int n, k, a[10], s; 

int main() { 
	scanf("%d %d", &n, &k); 
	for (int i = 0; i<n; i++)
		scanf("%d", a + i); 
	for (int i = n - 1; i >= 0; i--) 
	{ s += k / a[i]; k %= a[i]; }
	printf("%d", s); 
}