Title: Simple Distributed Locking with Redis
Date: 2024-05-24
Tags: Programming, Redis
Status: draft

I personally like using Redis for its flexibility and the way it simply enables the use of fundamental data structures that we all know and love in distributed applications. I've found it to be very good at bringing things together when you need coordination amongst a set of servers or containers running the same application.

One of these patterns that can be a quick little thing in Redis but more involved to implement with other databases is a distributed lock, and I'd like to illustrate a simple implementation of one with Redis here. This assumes the needs for a single-mode exclusive lock on a resource among any number of servers executing the same operation on that resource. The core mechanism of this lock is a check-and-set operation performed using a commonly agreed-upon key among several instances of an application. Each instance uses a distinct value to claim the lock and determine if it is holding the lock at any given time. It can claim the lock if no other instance of the application is holding the lock.

The simplest Redis lock can be managed with just the `SET` command. You can actually just run `SET $key $discriminator NX EX $timeout` and you've got a quick-and-dirty way to get timed exclusivity on whatever the lock represents. The `NX` part of that command makes `SET` operate as a check-and-set operation with the check being that the key does not have a value already. As such this single command can serve as our `lock` operation, but after acquisition you just have to wait for the lock to expire when you're done with it. A still-simple but more full-featured lock would offer some additional operations. Many users will expect an `unlock` operation and probably a `check` to see if the lock is held as well. Each of these operations can be written as a small Lua script to be invoked on the Redis server from your programming language of choice for a relatively portable implementation.

Acquiring the lock is a simple `SET` call, as previously described.

```lua
return redis.call('SET', KEYS[1], ARGV[1], 'NX', 'EX', ARGV[2])
```

Checking if the lock is held is a get and a comparision to the distinct lock value used by the caller.

```lua
local holder = redis.call('GET', KEYS[1])
return holder == ARGV[1]
```

Releasing the lock involves checking that the lock is currently held by the caller, then deleting the value of the lock key so that it is unheld again.

```lua
local holder = redis.call('GET', KEYS[1])
if holder ~= ARGV[1] then
    return 0
end
redis.call('DEL', KEYS[1])
return 1
```

A lock like this is easy to write and straightforward to use. It also has very modest requirements of Redis; it works well with a single-node or single-primary cluster. It is not bulletproof or foolproof but if you can tolerate or easily recovery from some duplicate work being performed this is a suitable design for a distributed lock.
