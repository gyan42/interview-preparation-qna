//* Imports */

import java.io.File;

//* Function :- To list the files in a directory. */

def getListOfFiles(dir: String):List[File] = {
	val d = new File(dir)
    if (d.exists && d.isDirectory) {
        d.listFiles.filter(_.isFile).toList
    } else {
        List[File]()
    }
}

//* Function :- To compute hash for a given string */

def hash(word:String) : Int = {var hash=0;for(ch <- word){hash=hash+ch.toInt};return hash}

//* Change the directory path  */ 

val files = getListOfFiles("C:\\Users\\sathis\\Downloads\\de-challenge-1-20210610T112227Z-001\\de-challenge-1\\test_dir");

val dict_rdd=files.map(file=>{val fileRdd=sc.textFile(file.toString).filter(!_.isEmpty).map(line => line.replaceAll("[^a-zA-Z0-9' ']+","")).flatMap(line=>line.split(" ")).filter(_.length !=0).map(word=> { var hash=0;for(ch <- word)
{hash=hash+ch.toInt};word -> hash}).distinct.collect.toMap;fileRdd})

val word_dict=dict_rdd.flatten.distinct.toMap

//* Broadcast the Dictionory */

var broadcast_dict=sc.broadcast(word_dict)


val sorted_Rdd=files.map(file=>{
val word_dict=broadcast_dict.value;
val fileRdd=sc.textFile(file.toString).filter(!_.isEmpty).map(line => line.replaceAll("[^a-zA-Z0-9' ']+","")).flatMap(line=>line.split(" ")).filter(_.length !=0).map(word=> (word_dict(word),file.getName.split("\\.")(0))).sortBy(x=>(x._1,x._2));fileRdd})


//* Print Word dictionary */ 

print(word_dict)

//* Print Inverted Index */ 

val inverted_index=sorted_Rdd.flatMap(x=>x.collect).groupBy(_._1).mapValues(x=> x.unzip._2.sorted).toSeq.sortBy(_._1)

print(inverted_index)
