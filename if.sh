#!/bin/bash
T1="foo"
if [ "$T1" = "bar" ]; then
    echo expression evaluated as true: "$T1" = "bar"
elif [ "$T1" = "foo" ]; then
    echo expression evaluated as true: "$T1" = "foo"
else
    echo expression evaluated as false
fi

