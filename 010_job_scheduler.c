#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

// Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

struct job_sched_args {
    int n;
    void (*f)();
};

void* job_scheduler(void* arguments)
{
    struct job_sched_args* args = (struct job_sched_args*)arguments;
    usleep(args->n * 1000);
    args->f();
}

void my_func()
{
    printf("my_func() has been called!\n");
}

int main()
{
    pthread_t scheduler_thread;
    struct job_sched_args job_args;

    job_args.n = 1000;
    job_args.f = &my_func;

    if (pthread_create(&scheduler_thread, NULL, &job_scheduler, &job_args)) {
        printf("Error creating thread...\n");
    }

    printf("Waiting...\n");

    if (pthread_join(scheduler_thread, NULL)) {
        printf("Error joining...\n");
    }

    return 0;
}
