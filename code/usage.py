from torchjd import autojac
from torchjd.aggregation import UPGrad

loss_fn = CrossEntropyLoss(reduction="none")
for input, target in loader:
    losses = loss_fn(model(input), target)
    autojac.backward(losses)
    autojac.jac_to_grad(model.parameters(), UPGrad())
    optimizer.step()
    optimizer.zero_grad()
