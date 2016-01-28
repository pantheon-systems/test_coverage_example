from fibonacci import fibonacci
from behave import given, when, then

# States


@given(u'a count of "{count}"')
def step_store_integer_count(context, count):
    context.count = int(count)
    context.f = fibonacci.Fibonacci()


@given(u'a non-integer count of "pantheon"')
def step_store_literal_count(context):
    context.count = 'pantheon'
    context.f = fibonacci.Fibonacci()

# Actions


@when(u'I call the fibonacci function')
def step_call_fibonacci(context):
    try:
        context.result = context.f.fib(context.count)
    except Exception as err:
        context.error = err

# Outcomes


@then(u'it should return a sequence "{sequence}"')
def step_return_sequence(context, sequence):
    expected_seq = [int(s) for s in sequence.split(',')]
    assert expected_seq == context.result


@then(u'the sequence should be a sequence of integers')
def step_sequence_is_integers(context):
    for i in context.result:
        assert isinstance(i, int)


@then(u'it should return an empty sequence')
def step_return_empty(context):
    assert context.result == []


@then(u'it should throw a TypeError exception')
def step_throw_error(context):
    assert isinstance(context.error, TypeError)
