import brownie

def test_commit_and_apply_transfer_gauge_controller_ownership(alice, factory, gauge_controller):
    assert gauge_controller.admin() == factory
    factory.commit_transfer_gauge_controller_ownership(alice, {"from": alice})
    factory.apply_transfer_gauge_controller_ownership({"from": alice})
    assert gauge_controller.admin() == alice
