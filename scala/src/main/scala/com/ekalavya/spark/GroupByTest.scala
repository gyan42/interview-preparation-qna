package com.ekalavya.spark

import org.apache.spark.{SparkConf, SparkContext}

object GroupByTest {
  def main(args: Array[String]) {
    val sparkConf = new SparkConf().setAppName("GroupBy Test")
    var numMappers = if (args.length > 0) args(0).toInt else 2
    var numKVPairs = if (args.length > 1) args(1).toInt else 1000
    var valSize = if (args.length > 2) args(2).toInt else 1000
    var numReducers = if (args.length > 3) args(3).toInt else numMappers

    println(numMappers)
    println(numKVPairs)
    println(valSize)
    println(numReducers)

    val sc = new SparkContext(sparkConf)

    val pairs1 = sc.parallelize(0 until numMappers, numMappers).flatMap { p =>
      val ranGen = new Random
      var arr1 = new Array[(Int, Array[Byte])](numKVPairs)
      for (i <- 0 until numKVPairs) {
        val byteArr = new Array[Byte](valSize)
        ranGen.nextBytes(byteArr)
        arr1(i) = (ranGen.nextInt(Int.MaxValue), byteArr)
      }
      arr1
    }.cache()
    println(numMappers)
    // Enforce that everything has been calculated and in cache
    println(numMappers)
    println(numKVPairs)
    println(valSize)
    println(numReducers)
    pairs1.count()

    println(pairs1.groupByKey(numReducers).count())
    println(numMappers)
    println(numKVPairs)
    println(valSize)
    println(numReducers)
    pairs1.count()

    sc.stop()
  }
}
