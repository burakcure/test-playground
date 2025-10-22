#include "Matrix.h"
#include <benchmark/benchmark.h>

// 100x100 matris çarpımı benchmark
static void BM_MatrixMultiplication(benchmark::State& state) {
    int size = static_cast<int>(state.range(0));
    Matrix a(size, size);
    Matrix b(size, size);

    // örnek veri dolduralım
    for (int i = 0; i < size; ++i)
        for (int j = 0; j < size; ++j) {
            a.data[i][j] = i + j;
            b.data[i][j] = i * j;
        }

    for (auto _ : state) {
        benchmark::DoNotOptimize(a*b);
    }
}
BENCHMARK(BM_MatrixMultiplication)->Arg(100)->Arg(200);

// 100x100 matris toplama benchmark
static void BM_MatrixAddition(benchmark::State& state) {
    int size = static_cast<int>(state.range(0));
    Matrix a(size, size);
    Matrix b(size, size);

    for (int i = 0; i < size; ++i)
        for (int j = 0; j < size; ++j) {
            a.data[i][j] = i + j;
            b.data[i][j] = i * j;
        }

    for (auto _ : state) {
        benchmark::DoNotOptimize(a+b);
    }
}
BENCHMARK(BM_MatrixAddition)->Arg(100)->Arg(200);

BENCHMARK_MAIN();
