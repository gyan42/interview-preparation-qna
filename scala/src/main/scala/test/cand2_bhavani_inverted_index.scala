import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkContext


object InvertedIndex{

 val docpath = "/docsets"
 val spark = SparkSession.builder.
      master(master).
      appName(name).  
      getOrCreate()

 val sc = spark.sparkContext
 val docset = sc.wholeTextFiles(docpath)
 //(doc_id,docconent) pairs
                 .flatMap(doc => doc._2.split("\\s+"))
                 .zipWithUniqueId()
//(word,word_id) pairs
	      .map(word => (word._2,doc._1)).sortByKey() 
// (word_id,doc_id) pairs sorted by word id
                 .groupByKey().mapValues(_.toList.sorted) 
//sorted list of docids for each word --> (word_id,[doc_id1,doc_id2..])
    		 .saveAsTextFile()
 spark.stop()

  /***
      cd /path/to/spark-2.4.4-bin-hadoop2.7
      sbin/start-all.sh
      bin/spark-shell --master spark://IMCHLT276:7077 --driver-memory 3G --executor-memory 3G --executor-cores 2

      Pump up the Driver and executor memory if OOM occurs, since broadcast variable is used part of the solution
    */


/***
  *
  * @param inPath Dataset input directoru
  * @param outPath Result output directory
  */
def invertedIndex(inPath: String, outPath: String): Unit = {

  val dataSet = sc.wholeTextFiles(inPath).repartition(32) // Increase this based on number of files in dataset

  val word2Index = dataSet.flatMap(pathText => pathText._2.split(" ")).distinct().zipWithUniqueId()
  val word2IndexBc = sc.broadcast(word2Index.collect().toMap) // {word -> id, ....}

  val wordIdDocIDPair = dataSet.flatMap{
    case (path: String, text: String) => {
      text.split(" ").map(word => (word, path.split("/").last)) // [(word, docID), ...]
    }
  }.mapPartitions( iter => { // Broadcast variable is access only once per partition
    val wordIndex = word2IndexBc.value
    iter.map{case (word, docID) => (wordIndex(word), docID)} // [(wordID, docID), ...]
  }).groupByKey().mapValues(_.toList.sorted).
    sortByKey() //[(wordID, []), ...]

  wordIdDocIDPair.saveAsTextFile(outPath)
}

val inPath = "/path/de-challenge-1-20210610T112227Z-001/de-challenge-1/dataset/"
val outPath = "/tmp/out2/"

invertedIndex(inPath=inPath, outPath=outPath)

  //  sbin/stop-all.sh

}



// bin/spark-shell --master spark://IMCHLT276:7077 --driver-memory 3G --executor-memory 3G --executor-cores 2