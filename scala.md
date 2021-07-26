# Scala

- How to avoid nulls?

```scala
Option[T] : Some(value) / None
Try[T]: Success(values) / Failure(exception)
Either[T1, T2] : Letf[T1], Right[T2]
```

```scala
val email: Try[String] = getEmail("bob")
val success: Boolean = if (email.isSuccess) {
  sendEmail(email.get)
} else {
  false
}

val email: Try[String] = getEmail("bob")
val success: Boolean = if (email.isSuccess) {
  sendEmail(email.get)
} else {
  false
}

val email: Try[String] = getEmail("bob")
val success = email.map(addr => sendEmail(addr)).toOption

val email: Left[String] = getEmail("bob")
val status: Either[String, String] = email match {
  case Failure(e) => Left("Couldn't get email address")
  case Success(e) => {
    if (sendEmail(e)) 
      Right(e) 
    else
      Left("Couldn't deliver invite")
  }
}
```