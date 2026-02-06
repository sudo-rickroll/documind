# Design Considerations

* Connection pools are not being used explicitly in this codebase, as redis-py creates and manages connection pools by default. However, if multiple redis namespaces were to be used, adding connection pools for the different namespaces would add to the ease of extensability of the class.

* Currently, the cache service depends on the redis client. This introduces tight coupling and makes the dependancy flow outward, and enhances the rigidity of the application with a tiered architecture. However, this would need to be refactored with the introduction of an interface that makes way for inversion of control and a much cleaner architecture.

* Context manager for redis client is tied with the application's lifecycle and not with the transaction's lifecycle, since this client is introduced as a singleton. This is because redis-py makes use of connection pooling (unlike NRedisStack which uses multiplexing) and the connection to redis becomes inactive and pooled after the transaction, even if the application server is running. Hence, separate connection objects are not necessary for every request or for every transaction. However, the repository class contains context management methods as utilities for use during unit testing if needed.

* Since redis-py establishes connection with client lazily, the cache server will need to be pinged before usage. This is why redis connection initialization is not an async operation, as it involves lazy binding.